# 導入 sys 模組
import sys
# 導入 keyword 模組
import keyword

# 利用 sys 模組中的 version_info 印出 Python 版次
print("Python version: ", sys.version_info)
# 利用 keyword 模組中的 kwlist 印出關鍵字
print("Python keywords: ", len(keyword.kwlist))
