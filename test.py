#!/usr/bin/env python3
import glob
import os
from cselector import multi_selector

# import aimage
# options = []
# preview = []
# values = []
# for f in glob.glob(os.path.expanduser("~/cg/*.jpg")):
#     preview += [aimage.load(f)]
#     options += [os.path.basename(f)]
#     values.append(0)
# values[3] = 1
# #values = None
# print(options)
# selected_array = multi_selector(
#     options=options, title="Title hogehoge", radio_button=True, option_values=values, preview=preview, preview_console=True
#     # options=options, title="Title hogehoge",all="all", option_values=values, preview=preview, preview_console=True
# )
# print(selected_array)  # [(<Index>,<Option>),(<Index>,<Option>),(<Index>,<Option>)....]

# exit(0)


# from cselector import selector

# i,o = selector(options=["ItemA", "ItemB", "ItemC"], title="Title hoge hoge.", default_index=2)
# print(i,o)  # (<Index>,<Option>)
# i,o = selector(options=["ItemA", "ItemB", "ItemC"], title="Title hoge hoge.", default_index=2)
# print(i,o)  # (<Index>,<Option>)

# import signal

# def signal_handler(sig, frame):
#     import cselector
#     print("@@@")
#     if cselector.G_end_function:
#         print("@@@")
#         cselector.G_end_function()
#     sys.exit(0)

# signal.signal(signal.SIGINT, signal_handler)




from cselector import yes_or_no

# ret = yes_or_no(question="Are you sure?", default="y")
# print(ret)  # True/False
ret = yes_or_no(question="Are you sure?", default=None)
print(ret)  # True/False

exit(0)

from cselector import multi_selector

options = []
for x in range(47):
    options.append("Item" + str(x))
selected_array = multi_selector(options=options, title="Title hogehoge")
print(selected_array)  # [(<Index>,<Option>),(<Index>,<Option>),(<Index>,<Option>)....]


from cselector import multi_selector

options = []
for x in range(47):
    options.append("Item" + str(x))
selected_array = multi_selector(
    options=options, title="Title hogehoge", all="All item title"
)
print(selected_array)  # [(<Index>,<Option>),(<Index>,<Option>),(<Index>,<Option>)....]


from cselector import multi_selector

options = []
for x in range(47):
    options.append("Item" + str(x))
selected_array = multi_selector(options=options, title="Title hogehoge", min_count=2)
print(selected_array)  # [(<Index>,<Option>),(<Index>,<Option>),(<Index>,<Option>)....]


from cselector import multi_selector

options = []
for x in range(47):
    options.append("Item" + str(x))
selected_array = multi_selector(options=options, title="Title hogehoge", split=20)
print(selected_array)  # [(<Index>,<Option>),(<Index>,<Option>),(<Index>,<Option>)....]
