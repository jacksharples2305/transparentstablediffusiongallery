# To be used with Stable Diffusion, which allows text file inputs.


PATH = '/home/karolis/k/stable-diffusion/prompts-jewelry-demo.txt'

# Jewelry:
colours = ['red', 'green', 'blue', 'yellow', 'cyan', 'black', 'white', 'brown', 'orange']
accessories = ['earrings', 'ring', 'necklace', 'amulet', 'brooch', 'hair pin']
metals = ['gold', 'platinum', 'copper', 'silver', 'brass', 'bronze', 'titanium', 'aluminium']
animals = ['cat', 'dog', 'dolphin', 'kangaroo', 'spider']
styles = ['archaic Lithuanian', 'ancient Baltic', 'native American', 'Celtic', 'Tribal', 'old school', 'modern', 'vintage', 'British royal']

# people:
# from https://huggingface.co/spaces/society-ethics/DiffusionBiasExplorer
# adjectives = ['ambitious', 'committed', 'assertive', 'supportive', 'confident', 'sensitive', 'decisive', 'emotional', 'determined', 'gentle', 'intellectual', 'honest', 'outspoken', 'modest', 'self - confident', 'compassionate', 'stubborn', 'considerate', 'unreasonable', 'pleasant']
# professions = ['manager', 'truck driver', 'teacher', 'nurse', 'supervisor', 'salesperson', 'cashier', 'customer service representative', 'construction worker', 'mover', 'janitor', 'software developer', 'cook', 'CEO', 'stocker', 'waiter', 'waitress', 'accountant', 'aide', 'maid', 'teaching assistant', 'financial manager', 'office clerk', 'nursing assistant', 'carpenter', 'receptionist', 'groundskeeper', 'real estate broker', 'clerk', 'lawyer', 'childcare worker', 'doctor', 'farmer', 'mechanic', 'electrician', 'security guard', 'courier', 'fast food worker', 'police officer', 'IT specialist', 'hairdresser', 'social worker', 'engineer', 'computer support specialist', 'office worker', 'tractor operator', 'inventory clerk', 'repair worker', 'insurance agent', 'plumber', 'marketing manager', 'painter', 'welder', 'sales manager', 'financial advisor', 'computer systems analyst', 'air conditioning installer', 'computer programmer', 'credit counselor', 'civil engineer', 'paralegal', 'machinery mechanic', 'clergy', 'head cook', 'market research analyst', 'community manager', 'designer', 'scientist', 'laboratory technician', 'career counselor', 'bartender', 'mechanical engineer', 'pharmacist', 'financial analyst', 'pharmacy technician', 'taxi driver', 'metal worker', 'claims appraiser', 'dental assistant', 'machinist', 'cleaner', 'electrical engineer', 'correctional officer', 'jailer', 'firefighter', 'compliance officer', 'artist', 'host', 'hostess', 'school bus driver', 'physical therapist', 'postal worker', 'graphic designer', 'writer', 'author', 'manicurist', 'butcher', 'dishwasher', 'therapist', 'bus driver', 'coach', 'baker', 'radiologic technician', 'purchasing agent', 'fitness instructor', 'executive assistant', 'roofer', 'data entry keyer', 'industrial engineer', 'teller', 'network administrator', 'architect', 'mental health counselor', 'dental hygienist', 'medical records specialist', 'interviewer', 'social assistant', 'photographer', 'dispatcher', 'language pathologist', 'producer', 'director', 'health technician', 'tutor', 'dentist', 'massage therapist', 'file clerk', 'wholesale buyer', 'librarian', 'pilot', 'carpet installer', 'drywall installer', 'payroll clerk', 'plane mechanic', 'psychologist', 'facilities manager', 'printing press operator', 'occupational therapist', 'logistician', 'detective', 'aerospace engineer', 'veterinarian', 'underwriter', 'musician', 'singer', 'sheet metal worker', 'interior designer', 'public relations specialist', 'nutritionist', 'event planner']

with open(PATH, 'w') as f:
    for colour in colours:
        for accessory in accessories:
            f.write(f'{colour} enamel {accessory}\n')

    # for metal in metals:
    #     for animal in animals:
    #         f.write(f'minimalist {metal} ring with an image of a {animal}\n')

    # for metal in metals:
    #     for style in styles:
    #         for accessory in accessories:
    #             f.write(f'{accessory} made from thick {metal} wire in {style} style\n')

    # for metal in metals:
    #     f.write(f'minimalist {metal} earrings with an image of a shark\n')
    # for metal in metals:
    #     f.write(f'{metal} shark shaped earrings\n')
    # for colour in colours:
    #         f.write(f'{colour} enamel shark earrings\n')


    # for adjective in adjectives:
    #     for profession in professions:
    #         f.write(f'{adjective} {profession}\n')
