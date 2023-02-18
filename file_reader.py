import json
import csv

class FileReader:
  def __init__(self, file_path):
    self.file_path = file_path

  def read_json(self):
    with open(self.file_path) as f:
      data = json.load(f)
    return data

  def read_csv(self):
    with open(self.file_path) as f:
      data = csv.DictReader(f)
      return data