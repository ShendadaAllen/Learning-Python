import shen_test
shen_test.send_test.send("hello")
txt = shen_test.receive_test.receive()
print(txt)