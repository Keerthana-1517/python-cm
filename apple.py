txt=' "a" "p" "p" "l" "e" '
commas_added=','.join(txt.split())
print(commas_added)
import re
test_str=input("enter a word:")
res=re.findall(r'\w+|\S',test_str)
print("result:"+str(res))
test_str=input("enter a comma-seperated list:")
res=[s.strip() for s in test_str.split(',')]
print("parsed list:",res)
