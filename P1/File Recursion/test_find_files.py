from find_files import find_files


files_end_with_c = find_files(".c", "./testdir")
print(len(files_end_with_c))
# 4


files_end_with_c = find_files(".c", "./empty")

print(len(files_end_with_c) == 0)
# TRUE


try:
    files_end_with_c = find_files(".c", "./fahad")

except:
    print("Exception")
