from azure.servicebus import ServiceBusClient, ServiceBusMessage

# Replace with your own connection string and queue name
connection_string = "<connection string>"
queue_name = "my-demo-queue"

def send_messages_to_queue():
    try:
        # Create a Service Bus client
        servicebus_client = ServiceBusClient.from_connection_string(connection_string)

        # Create a sender for the queue
        sender = servicebus_client.get_queue_sender(queue_name)

        # Create a message
        message = ServiceBusMessage("Hello from Java!")

        # Send the message to the queue
        sender.send_messages(message)
        print("Message sent successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# sending batch of messages
def send_batch_messages_to_queue():

    # Create a Service Bus client
    servicebus_client = ServiceBusClient.from_connection_string(connection_string)

    # Create a sender for the queue
    sender = servicebus_client.get_queue_sender(queue_name)

    batch_message = sender.create_message_batch()

    for i in range(10):
        try:
            # add messages to the batch 
            batch_message.add_message(ServiceBusMessage("This is the sample message"))
        except ValueError:
                # ServiceBusMessageBatch object reaches max_size.
                # New ServiceBusMessageBatch object can be created here to send more data.
                break

    # send the messages to the queue
    sender.send_messages(batch_message)   
    print("Send the batch of 10 messages")
    


if __name__ == "__main__":
    #send_messages_to_queue()
    send_batch_messages_to_queue()
