books = {"Margaret Atwood" : ["The Handmaid's Tale"], "J.R.R. Tolkien" : ["The Hobbit", "The Fellowship of The Ring", "The Two Towers", "The Return of the King"], "Roald Dahl" : ["Charlie and the Chocolate Factory"], "R.F. Kuang" : ["The Poppy War", "The Dragon Republic", "The Burning God"]}

author_name = input("Enter author's name: ")
  

print("Books by this author:",(", ".join(books[author_name])))


