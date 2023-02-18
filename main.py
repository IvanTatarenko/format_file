from file_reader import FileReader
from column_search import ColumnSearch

from simple_term_menu import TerminalMenu
import os
import tqdm
import json

DIR_PATH = 'data/input'
COLUMN_NAME = ['do not need',
               'phone',
               'email',
               'name',
               'address',
               'telegram_id',
               'telegram_username',
               'ip',
               'user_agent',
               'login',
               'password',
               'birthday',
               'snils',
               'inn',
               'passport']

def file_format_menu():
  options = ["json", "csv"]
  terminal_menu = TerminalMenu(options)
  file_format = terminal_menu.show()
  return options[file_format]

def rename_column(data):
  column_name_file = {}
  # Перебір назв рядків
  for column_name in data[0]:
    auto_column_name = ColumnSearch(column_name).search()
    if auto_column_name:
      column_name_file[column_name] = auto_column_name
      continue
    # Показуємо 10 рядок
    print(data[10])
    # Показуємо назву стовпцю який треба змнити
    print(column_name)
    column_name_menu = TerminalMenu(COLUMN_NAME)
    new_column_name = column_name_menu.show()
    if COLUMN_NAME[new_column_name] == 'do not need':
      continue
    column_name_file[column_name] = COLUMN_NAME[new_column_name]
  return column_name_file

def save_new_json(filename, rename_column_dict, data):
  # Замінюємо назви колонок в словнику даних
  for row in data:
    for old_name, new_name in rename_column_dict.items():
      if old_name in row:
        row[new_name] = row.pop(old_name)

  # Видаляємо колонки, яких немає в словнику даних
  for row in data:
    for column_name in list(row.keys()):
      if column_name not in rename_column_dict.values():
        del row[column_name]

  print(rename_column_dict)
  print(data)  
  # Зберігаємо оновлені дані в JSON-файлі
  with open(f'data/output/{filename}', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


def main():
  file_format = file_format_menu()
  if file_format == 'json':
    for filename in tqdm.tqdm(os.listdir(DIR_PATH)):
      file_path = os.path.join(DIR_PATH, filename)
      # Отримання файлу з данними
      json_data = FileReader(file_path).read_json()
      # Визанчаємо нові назви стовпців
      rename_column_dict = rename_column(json_data)
      print(rename_column_dict)
      save_new_json(filename, rename_column_dict, json_data)
  elif file_format == 'csv':
    print('c')
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()