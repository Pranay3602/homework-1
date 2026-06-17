page=(input("is all your pages cleared and closed y/n"))
saved=(input("is all your important documants saved y/n"))
if page and saved=="y":
    print("shutdown starting")
elif page and saved=="n":
    print("not able to shutdown")
else:
    print("not a valid answer")