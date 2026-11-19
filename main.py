def test_login(user, password):
    if user == "admin" and password == "1234":
        print("SUCCESS")
    else:
        print("FAILED")

test_login("admin", "1234")
test_login("user", "0000")
test_login("user1", "1111")
test_login("user2", "2222")
