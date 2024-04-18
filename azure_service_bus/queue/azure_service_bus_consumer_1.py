from azure.servicebus import ServiceBusClient, ServiceBusMessage

connection_str = '<connection string>'
queue_name = 'my-demo-queue'

# Create a Service Bus client
servicebus_client = ServiceBusClient.from_connection_string(connection_str)

# Get the Service Bus Receiver client for the queue
receiver_client = servicebus_client.get_queue_receiver(queue_name)

# Receive messages
messages = receiver_client.receive_messages(max_message_count=10, max_wait_time=5)

for msg in messages:
    print("Consumer 1 : Received message:  ", msg)
    # Complete the message so that it's not received again.
    receiver_client.complete_message(msg)

# Close the clients
receiver_client.close()
servicebus_client.close()
