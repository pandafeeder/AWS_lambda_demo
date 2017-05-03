import fifty_sound

if __name__ == '__main__':
    event = {
            'httpMethod': 'GET',
            'queryStringParameters': {'char': 'a'},
            }
    print(fifty_sound.lambda_handler(event, None))
