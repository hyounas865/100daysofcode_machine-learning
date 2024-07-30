import re
fav_qawali='bottal khuli hai raqs mai jaam e sharab hai aye mai kasho tumhari dua kaam yab hai'
word_to_find=(r'sharabkabab')
search_word=re.search(word_to_find,fav_qawali)
if search_word:
    print('word found')
else:
    print('word not found')    
