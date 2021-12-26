from mdutils.mdutils import MdUtils
from mdutils import Html
import glob
from posixpath import basename

def get_file_names():
    names = []
    for file in glob.glob('solutions/*.py'):
        name = basename(file)
        names.append(name)
    return names

def get_num(x):
    # input: str -> day2.py, day11.py, day10.py
    # output: int -> 2, 11, 10
    return int(x.split(".")[0][3:])

files = sorted(get_file_names(), key=get_num)

mdFile = MdUtils(file_name='README.md', title='My solutions for Advent of Code λy.2021')
mdFile.new_paragraph("https://adventofcode.com/2021")
for file in files:
    name = file.split(".")[0].capitalize()
    link = mdFile.new_inline_link(f"solutions/{file}", text="solution")
    mdFile.new_line(text=f"* {name} {link}.")

mdFile.create_md_file()