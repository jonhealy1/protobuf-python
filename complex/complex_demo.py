import complex_pb2 as complex_pb2

complex_message = complex_pb2.ComplexMessage()

# wrong
# dummy_message = complex_pb2.DummyMessage()
# dummy_message.id = 123
# dummy_message.name = "Jon"
# complex_message.one_dummy = dummy_message

complex_message.one_dummy.id = 123
complex_message.one_dummy.name = "Jon"

first_dummy = complex_message.multiple_dummy.add()
first_dummy.id = 456
first_dummy.name = 'Sam'

complex_message.multiple_dummy.add(id = 567, name='Lisa')

third_dummy = complex_pb2.DummyMessage()
third_dummy.id = 999
third_dummy.name = 'Bob'
complex_message.multiple_dummy.extend([third_dummy])

third_dummy.id=111 #doesn't work
print(complex_message)