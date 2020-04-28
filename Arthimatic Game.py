import random
import time
import decimal 


class AG:
    def __init__(self,nq):
        self.nq=nq
    def gq(self):
        op_1=random.randint(1,30)
        op_2=random.randint(1,30)
        op=random.choice(['+','-','*','//'])
        if op=='+':
            ans=op_1+op_2
        if op=='-':
            ans=op_1-op_2
        if op=='*':
            ans=op_1*op_2
        if op=='//':
            ans=round((op_1/op_2),2)
        qus=str(op_1)+' '+op+' '+str(op_2)
        return qus,ans
    def play_game(self):
        num_crt=0
        s_t=time.time()
        for i in range(self.nq):
            print('Question '+str(i+1)+':')
            qus,ans=self.gq()
            print(qus)
            usr_ans=float(input('Enter Your Answer :'))
            if usr_ans == ans:
                num_crt+=1
                print('Correct Answer')
            else :
                print('Wrong Answer, the correct Answer is'+str(ans))
        e_t=time.time()
        print('you got' + str(num_crt)+'Answer correct.')
        print('you used {:.3f} seconds '.format(e_t-s_t))
        
ng=AG(10)
ng.play_game()
