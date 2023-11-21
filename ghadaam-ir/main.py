#in the name of god

#coming soon

# desgined by sahandmohammadrezaii and ghadaam team

import re
import long_responses as long

for i in range(1):
   print("              به هوش مصنوعی ساخته شده توسط تیم ویژه قادم خوش آمدید")

#cli-1

for i in range(1):
   print("")
   
#cli-2
   
for i in range(1):
    print("")

#cli-3

for i in range(1):
    print("")
    
#wellcome-massage

for i in range(1):
    print("ghadaam-ir : سلام من قادم آی آر هستم من آماده خدمت به شما در هر لحظه ای هستم")

#cli-4

for i in range(1):
    print("");
    
#cli-5

for i in range(1):
    print("");
    
#cli-6

for i in range(1):
    print("");

#massage-components

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

#massage-if & else

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1


    percentage = float(message_certainty) / float(len(recognised_words))


    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break


    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

#write-the-massage-ghadaam-ir    => black.cli   <+>   console.log("hello world I am ghadaam-ir")

    response('سلام', ['hello', 'سلام', 'hi', 'salam',], single_response=True)
    response('به اميد ديدار', ['به اميد ديدار', 'bye', 'goodbye', 'خداحافظ', 'باي',], single_response=True)
    response('من هيچ گونه احساس ندارم و نمي توانم مانند انسان ها حس داشته باشم', ['حالت چطوره', 'خوبي', 'how are you', 'حالت خوبه '], required_words=['چطوري'])
    response('خوش آمدید به قادم آی آر', ['thank', 'thanks'], single_response=True)
    response('متشکرم از شما', ['ممنون', 'دستت درد نکنه', 'با تشکر از شما',], required_words=['code', 'palace'])


    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)


    return long.unknown() if highest_prob_list[best_match] < 1 else best_match



def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response



while True:
    print('ghadaam-ir : ' + get_response(input('شما : ')))
    
while False:
    print('ghadaam-ir = > def datebassment.getbyelement : ' + get_response(input('user = > api-cli: ')))
