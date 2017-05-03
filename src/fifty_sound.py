import json

fifty_sound_collection = (
    {'char': 'a',  'hiragana':'あ', 'katagana':'ア'},
    {'char': 'i',  'hiragana':'い', 'katagana':'イ'},
    {'char': 'u',  'hiragana':'う', 'katagana':'ウ'},
    {'char': 'e',  'hiragana':'え', 'katagana':'エ'},
    {'char': 'o',  'hiragana':'お', 'katagana':'オ'},
    {'char': 'ka', 'hiragana':'か', 'katagana':'カ'},
    {'char': 'ki', 'hiragana':'き', 'katagana':'キ'},
    {'char': 'ku', 'hiragana':'く', 'katagana':'ク'},
    {'char': 'ke', 'hiragana':'け', 'katagana':'ケ'},
    {'char': 'ko', 'hiragana':'こ', 'katagana':'コ'},
    {'char': 'sa', 'hiragana':'さ', 'katagana':'サ'},
    {'char': 'si', 'hiragana':'し', 'katagana':'シ'},
    {'char': 'su', 'hiragana':'す', 'katagana':'ス'},
    {'char': 'se', 'hiragana':'せ', 'katagana':'セ'},
    {'char': 'so', 'hiragana':'そ', 'katagana':'ソ'},
    {'char': 'ta', 'hiragana':'た', 'katagana':'タ'},
    {'char': 'ti', 'hiragana':'ち', 'katagana':'チ'},
    {'char': 'tu', 'hiragana':'つ', 'katagana':'ツ'},
    {'char': 'te', 'hiragana':'て', 'katagana':'テ'},
    {'char': 'to', 'hiragana':'と', 'katagana':'ト'},
    {'char': 'na', 'hiragana':'な', 'katagana':'ナ'},
    {'char': 'ni', 'hiragana':'に', 'katagana':'ニ'},
    {'char': 'nu', 'hiragana':'ぬ', 'katagana':'ヌ'},
    {'char': 'ne', 'hiragana':'ね', 'katagana':'ネ'},
    {'char': 'no', 'hiragana':'の', 'katagana':'ノ'},
    {'char': 'ha', 'hiragana':'は', 'katagana':'ハ'},
    {'char': 'hi', 'hiragana':'ひ', 'katagana':'ヒ'},
    {'char': 'hu', 'hiragana':'ふ', 'katagana':'フ'},
    {'char': 'he', 'hiragana':'へ', 'katagana':'ヘ'},
    {'char': 'ho', 'hiragana':'ほ', 'katagana':'ホ'},
    {'char': 'ma', 'hiragana':'ま', 'katagana':'マ'},
    {'char': 'mi', 'hiragana':'み', 'katagana':'ミ'},
    {'char': 'mu', 'hiragana':'む', 'katagana':'ム'},
    {'char': 'me', 'hiragana':'め', 'katagana':'メ'},
    {'char': 'mo', 'hiragana':'も', 'katagana':'モ'},
    {'char': 'ya', 'hiragana':'や', 'katagana':'ヤ'},
    {'char': 'yu', 'hiragana':'ゆ', 'katagana':'ユ'},
    {'char': 'yo', 'hiragana':'よ', 'katagana':'ヨ'},
    {'char': 'ra', 'hiragana':'ら', 'katagana':'ラ'},
    {'char': 'ri', 'hiragana':'り', 'katagana':'リ'},
    {'char': 'ru', 'hiragana':'る', 'katagana':'ル'},
    {'char': 're', 'hiragana':'れ', 'katagana':'レ'},
    {'char': 'ro', 'hiragana':'ろ', 'katagana':'ロ'},
    {'char': 'wa', 'hiragana':'わ', 'katagana':'ワ'},
    {'char': 'wo', 'hiragana':'を', 'katagana':'ヲ'},
    {'char': 'nn', 'hiragana':'ん', 'katagana':'ン'},
)

fifty_sound_index = {
    'a':  {'char': 'a',  'hiragana': 'あ', 'katagana': 'ア'},
    'i':  {'char': 'i',  'hiragana': 'い', 'katagana': 'イ'},
    'u':  {'char': 'u',  'hiragana': 'う', 'katagana': 'ウ'},
    'e':  {'char': 'e',  'hiragana': 'え', 'katagana': 'エ'},
    'o':  {'char': 'o',  'hiragana': 'お', 'katagana': 'オ'},
    'ka': {'char': 'ka', 'hiragana': 'か', 'katagana': 'カ'},
    'ki': {'char': 'ki', 'hiragana': 'き', 'katagana': 'キ'},
    'ku': {'char': 'ku', 'hiragana': 'く', 'katagana': 'ク'},
    'ke': {'char': 'ke', 'hiragana': 'け', 'katagana': 'ケ'},
    'ko': {'char': 'ko', 'hiragana': 'こ', 'katagana': 'コ'},
    'sa': {'char': 'sa', 'hiragana': 'さ', 'katagana': 'サ'},
    'si': {'char': 'si', 'hiragana': 'し', 'katagana': 'シ'},
    'su': {'char': 'su', 'hiragana': 'す', 'katagana': 'ス'},
    'se': {'char': 'se', 'hiragana': 'せ', 'katagana': 'セ'},
    'so': {'char': 'so', 'hiragana': 'そ', 'katagana': 'ソ'},
    'ta': {'char': 'ta', 'hiragana': 'た', 'katagana': 'タ'},
    'ti': {'char': 'ti', 'hiragana': 'ち', 'katagana': 'チ'},
    'tu': {'char': 'tu', 'hiragana': 'つ', 'katagana': 'ツ'},
    'te': {'char': 'te', 'hiragana': 'て', 'katagana': 'テ'},
    'to': {'char': 'to', 'hiragana': 'と', 'katagana': 'ト'},
    'na': {'char': 'na', 'hiragana': 'な', 'katagana': 'ナ'},
    'ni': {'char': 'ni', 'hiragana': 'に', 'katagana': 'ニ'},
    'nu': {'char': 'nu', 'hiragana': 'ぬ', 'katagana': 'ヌ'},
    'ne': {'char': 'ne', 'hiragana': 'ね', 'katagana': 'ネ'},
    'no': {'char': 'no', 'hiragana': 'の', 'katagana': 'ノ'},
    'ha': {'char': 'ha', 'hiragana': 'は', 'katagana': 'ハ'},
    'hi': {'char': 'hi', 'hiragana': 'ひ', 'katagana': 'ヒ'},
    'hu': {'char': 'hu', 'hiragana': 'ふ', 'katagana': 'フ'},
    'he': {'char': 'he', 'hiragana': 'へ', 'katagana': 'ヘ'},
    'ho': {'char': 'ho', 'hiragana': 'ほ', 'katagana': 'ホ'},
    'ma': {'char': 'ma', 'hiragana': 'ま', 'katagana': 'マ'},
    'mi': {'char': 'mi', 'hiragana': 'み', 'katagana': 'ミ'},
    'mu': {'char': 'mu', 'hiragana': 'む', 'katagana': 'ム'},
    'me': {'char': 'me', 'hiragana': 'め', 'katagana': 'メ'},
    'mo': {'char': 'mo', 'hiragana': 'も', 'katagana': 'モ'},
    'ya': {'char': 'ya', 'hiragana': 'や', 'katagana': 'ヤ'},
    'yu': {'char': 'yu', 'hiragana': 'ゆ', 'katagana': 'ユ'},
    'yo': {'char': 'yo', 'hiragana': 'よ', 'katagana': 'ヨ'},
    'ra': {'char': 'ra', 'hiragana': 'ら', 'katagana': 'ラ'},
    'ri': {'char': 'ri', 'hiragana': 'り', 'katagana': 'リ'},
    'ru': {'char': 'ru', 'hiragana': 'る', 'katagana': 'ル'},
    're': {'char': 're', 'hiragana': 'れ', 'katagana': 'レ'},
    'ro': {'char': 'ro', 'hiragana': 'ろ', 'katagana': 'ロ'},
    'wa': {'char': 'wa', 'hiragana': 'わ', 'katagana': 'ワ'},
    'wo': {'char': 'wo', 'hiragana': 'を', 'katagana': 'ヲ'},
    'nn': {'char': 'nn', 'hiragana': 'ん', 'katagana': 'ン'}
}

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res, ensure_ascii=False),
        'headers': {
        'Content-Type': 'application/json',
        }
    }

def lambda_handler(event, context):
    global fifty_sound_dict
    operations = {
        'GET': lambda x: fifty_sound_index.get(x) or fifty_sound_collection
    }
    operation = event['httpMethod']
    if operation in operations:
        if not (event['queryStringParameters'] or event['pathParameters']):
            payload = None
        elif event['queryStringParameters']:
            payload = event['queryStringParameters'].get('char')
        elif event['pathParameters']:
            payload = event['pathParameters'].get('char')
        return respond(None, operations[operation](payload))
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))


