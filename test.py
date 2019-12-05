
from cselector import selector

selected = selector(options=["ItemA","ItemB","ItemC"],title="Title hoge hoge.")
print(selected) # (<Index>,<Option>)


from cselector import multi_selector

options = []
for x in range(47):
    options.append("Item"+str(x))
selected_array = multi_selector(options=options,title="Title hogehoge")
print(selected_array) # [(<Index>,<Option>),(<Index>,<Option>),(<Index>,<Option>)....]


from cselector import multi_selector

options = []
for x in range(47):
    options.append("Item"+str(x))
selected_array = multi_selector(options=options,title="Title hogehoge",all="All item title")
print(selected_array) # [(<Index>,<Option>),(<Index>,<Option>),(<Index>,<Option>)....]


from cselector import multi_selector

options = []
for x in range(47):
    options.append("Item"+str(x))
selected_array = multi_selector(options=options,title="Title hogehoge",min_count=2)
print(selected_array) # [(<Index>,<Option>),(<Index>,<Option>),(<Index>,<Option>)....]


from cselector import multi_selector

options = []
for x in range(47):
    options.append("Item"+str(x))
selected_array = multi_selector(options=options,title="Title hogehoge",split=20)
print(selected_array) # [(<Index>,<Option>),(<Index>,<Option>),(<Index>,<Option>)....]


from cselector import yes_or_no
ret = yes_or_no(question="Do you do machine learning?",default="y")
print(ret) # True/False

import aimage
import glob
import os
from cselector import multi_selector
options = []
preview = []
for f in glob.glob(os.path.expanduser("~/cg/*.jpg")):
    preview += [aimage.load(f)]
    options += [os.path.basename(f)]
print(options)
selected_array = multi_selector(options=options,title="Title hogehoge",preview=preview,preview_console=True)
print(selected_array) # [(<Index>,<Option>),(<Index>,<Option>),(<Index>,<Option>)....]
