text = 'X-DSPAM-Confidence:    0.8475'
colon = text.find(':')
tmp = text[colon+1:]
tmp = tmp.strip()
nr = float(tmp)
print(nr)
