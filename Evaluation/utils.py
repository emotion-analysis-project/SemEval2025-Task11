import os
import sys
import numpy as np
import scipy.stats as ss
from sklearn.metrics import f1_score, jaccard_score

import warnings
warnings.filterwarnings('ignore')

def get_task_details(submission_file):
  try:
    language = submission_file.split('_')[1]
    task = submission_file.split('_')[2].split('.')[0]
    return language, task
  except IndexError:
    exit('Submission file name is not in the correct format, it should have the format "pred_langcode_taskname.csv".')

def check_if_data_is_released(language):
  if language in open('../langs.txt').read().splitlines():
    return True

def check_file_name(file_path):
  checklist = []
  file_name = os.path.basename(file_path)

  lang, task = get_task_details(file_name)

  if not (os.path.exists(file_path) or os.path.isfile(file_path)):
    checklist.append(['Submission file.', 'Fail', 'Not found or invalid.'])
  else:
    checklist.append(['Submission file.', 'Pass', f'Found valid file: {file_name}'])
  if not file_name.endswith('.csv'):
    checklist.append(['File format.', 'Fail', 'Not a csv file.'])
  else:
    checklist.append(['File format.', 'Pass', 'CSV file.'])
  
  if not file_name.startswith('pred_'):
    checklist.append(['File name.', 'Fail', 'Should start with "pred_"'])
  if not lang:
    checklist.append(['Language code.', 'Fail', 'Language code not found after "pred_".'])
  else:
    checklist.append(['Language code.', 'Pass', f'Language code: {lang}'])
  if not task in ['a', 'b', 'c']:
    checklist.append([f'Task name.', 'Fail', 'Should contain the task name ("a", "b", or "c") after the language name.'])
  else:
    checklist.append([f'Task name.', 'Pass', f'Task: {task.upper()}'])

  if len(checklist) == 3:
    checklist.append(['Submission file name.', 'Pass', ''])

  return checklist

def are_lists_equal(list1, list2):
  return [x.lower() for x in list1] == [x.lower() for x in list2]

def check_files(gold, pred):
  gold_lines = open(gold).read().splitlines()
  pred_lines = open(pred).read().splitlines()

  valid_header = gold_lines[0].split(',')
  pred_header = pred_lines[0].split(',')

  if not are_lists_equal(valid_header, pred_header):
    sys.exit(f'Invalid submission header: {pred_header}. Your submission should have an "id" column first and {len(valid_header) - 1} columns for emotions: {valid_header[1:]}, in this order.')

  if len(gold_lines) != len(pred_lines):
    sys.exit(f'Predictions ({os.path.basename(pred)}) and gold data have different number of lines.')

  print('\nFiles format checked successfully\n')

  return gold_lines, pred_lines

def populate_data_dict(gold_lines, pred_lines, label_range):
  data_dic = {}
  
  for row in gold_lines[1:]:
    parts = row.split(',')
    data_dic[parts[0]] = [tuple(map(int, parts[1:label_range]))]
  
  for row in pred_lines[1:]:
    parts = row.split(',')
    if parts[0] in data_dic:
      try:
        data_dic[parts[0]].append(tuple(map(int, parts[1:label_range])))
      except ValueError:
        data_dic[parts[0]].append((0,) * (label_range - 1))
    else:
      sys.exit(f'Invalid tweet id: {parts[0]} found in submitted predictions file.')

  return data_dic

def compute_scores(data_dic):
  gold_scores = [labels[0] for labels in data_dic.values() if len(labels) == 2]
  pred_scores = [labels[1] for labels in data_dic.values() if len(labels) == 2]

  if len(gold_scores) != len(pred_scores):
    sys.exit(f"Error: Mismatch in number of valid predictions and gold labels.")

  return np.array(gold_scores), np.array(pred_scores)

def evaluate(gold_lines, pred_lines):

  data_dic = populate_data_dict(gold_lines, pred_lines, 8)

  y_true, y_pred = compute_scores(data_dic)

  acc = jaccard_score(y_true, y_pred, average='samples')
  f1_micro = f1_score(y_true, y_pred, average='micro')
  f1_macro = f1_score(y_true, y_pred, average='macro')

  return acc, f1_micro, f1_macro

def evaluate_b(gold_lines, pred_lines):
  
  emotions = gold_lines[0].split(',')[1:]
  data_dic = populate_data_dict(gold_lines, pred_lines, len(emotions) + 1)

  emotions_data_dict = {emotion: {'gold': [], 'pred': []} for emotion in emotions}
  for gold_line, pred_line in zip([d[0] for d in data_dic.values()], [d[1] for d in data_dic.values()]):
    for i, emotion in enumerate(emotions):
      emotions_data_dict[emotion]['gold'].append(float(gold_line[i]))
      emotions_data_dict[emotion]['pred'].append(float(pred_line[i]))

  emotion_r = {
    emotion: round(ss.pearsonr(emotions_data_dict[emotion]['gold'], emotions_data_dict[emotion]['pred'])[0], 4)
      for emotion in emotions
  }

  return emotion_r