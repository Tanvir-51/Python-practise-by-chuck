text = "X-DSPAM-Confidence:    0.8475"

cpos = text.find(':')

mpart = text[cpos+5:]

value = float(mpart)
print(value)