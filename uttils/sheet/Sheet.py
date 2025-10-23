import gspread
from google.oauth2.service_account import Credentials
import os
from datetime import datetime
from gspread.cell import Cell
from gspread.worksheet import Worksheet
import time 
from typing import Tuple, Dict, Any
from itertools import zip_longest
from gspread.utils import rowcol_to_a1
from config_reader import config

class Sheet:
    HEADERS = [
        "data",	"id", "username",
        "fullname", "address", "start-time",
        "end-time", "duration", "comment", "status"
    ]
    
    def __init__(self) -> None:    
        SERVICE_FILE = config.google_account_path
        SHEET_NAME = config.sheet_name
        SCOPES = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = Credentials.from_service_account_file(SERVICE_FILE, scopes=SCOPES)
        gc = gspread.authorize(creds)
        self.sheet: Worksheet = gc.open(SHEET_NAME).sheet1
        self.headers = self.HEADERS
    
    def cellToRow(self, cell: Cell):
        row_index = cell.row
        row_values = self.sheet.row_values(row_index)
        row_dict = dict(zip_longest(self.headers, row_values, fillvalue=""))
        row_dict["_index"] = row_index
        return row_dict
    
    def getLastUserRow(self, user_id: int) -> Dict[Any, Any]:
        user_index = self.headers.index("id") + 1
        col_values = self.sheet.col_values(user_index)
        for i, value in enumerate(reversed(col_values), start=1):
            if str(value) == str(user_id):
                row_index = len(col_values) - i + 1
                return self.cellToRow(Cell(row=row_index, col=user_index))
        
        return {}
        
    def startSession(self, user_id: int, username: str, name: str, geo: str) -> None:
        current_day = datetime.now()
        today = current_day.strftime("%Y-%m-%d") 
        current_time =  current_day.strftime("%H:%M")
        row = self.getLastUserRow(user_id)
        if row.get("status") == "open":
            return 
            
        self.sheet.append_row([today, user_id, username, name, geo, current_time, "", "" , "", "open"], value_input_option='USER_ENTERED')
    
    
    def closeSession(self, user_id: int) -> Tuple[int, str]:
        row = self.getLastUserRow(user_id)

        if row.get("status") == "open":            
            status_index = self.headers.index("status") + 1
            end_time_index = self.headers.index("end-time") + 1
            start_time_index = self.headers.index("start-time") + 1
            duration_index = self.headers.index("duration") + 1 
            
            current_day = datetime.now()
            current_time =  current_day.strftime("%H:%M") 
            
            self.sheet.update_cells(
                [
                    Cell(row["_index"], end_time_index, current_time),
                    Cell(row["_index"], status_index, "close"),
                ], value_input_option='USER_ENTERED')
            
            start_col_letter = rowcol_to_a1(row=1, col=start_time_index)[0:-1]
            end_col_letter = rowcol_to_a1(row=1, col=end_time_index)[0:-1]
            
            formula = "={end}{row}-{start}{row}".format(
                start=start_col_letter, 
                end=end_col_letter, 
                row=row["_index"]
            )
                 
            self.sheet.update_cell(row["_index"], duration_index, formula)
            duration = self.sheet.cell(row["_index"], duration_index)
            return row["_index"] - 1, str(duration.value)     
        
        return 0, ""
    
    def commentSession(self, user_id: int, comment: str):
        row = self.getLastUserRow(user_id)

        if row.get("status") == "close":
            status_index = self.headers.index("comment") + 1
            self.sheet.update_cell(row["_index"], status_index, "'{}".format(comment))
    
    def cancelSession(self, user_id: int):
        row = self.getLastUserRow(user_id)
    
        if row.get("statёus") == "open":
            status_index = self.headers.index("status") + 1
            self.sheet.update_cell(row["_index"], status_index, "cancel")
