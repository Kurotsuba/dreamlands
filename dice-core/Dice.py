class Dice:
    class Charactor:
        def __init__(name):
            this.name = name
            this.rate_dict = {}



    def __init__(rand_gen, chara_reader):
        this.rand_gen = rand_gen
        this.chara_reader = chara_reader
        this.chara_list = {}
    
    def basic_roll(uplimit=100):
        return this.rand_gen.roll(uplimit)
    
    def roll(chara_name='', target_name=''):
        roll_result = basic_roll()
        if (chara_name == '' and target_name == ''):
            return '{}'.format(roll_result)
        elif (chara_name != '' and target_name != ''):
            target = this.chara_list[chara_name].rate_dict[target_name]
            hard_target = int(0.5 * target)
            extreme_target = int(0.2 * target)
            
            if(roll_result <= target and roll_result > hard_target):
                return 'success'
            elif(roll_result <= hard_target and roll_result > extreme_target):
                return 'hard_success'
            elif (roll_result <= extreme_target):
                return 'extreme_success'
            else:
                return 'miss'
    
