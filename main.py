meme_dict = {
            "haha": "ketawa",
            "p": "pemulai chat",
            }
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
if word in meme_dict.keys():
    print("kata ditemukan")
else:
    print("kata tidak ditemukan")
