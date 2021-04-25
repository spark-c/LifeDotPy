
import datetime as dt
import MemoryBank

class Puppy():
    base_clock = 90 # seconds
    ...

    def __init__(self, personality_modifiers):
        self.memories = MemoryBank(personality_modifiers)
        self.clock = dt.timedelta(seconds=\
            Puppy.base_clock * self.personality_modifiers['independence'])
        self.time_reference_point = dt.now()
        ... 

    def update_time_reference(self):
        self.time_reference_point = dt.now()

    def routine_checks(self):
        needs_report['Human'] = self.check_for_human()
        ...
        return needs_report

    def check_for_human(self):
        for stimulus in self.memories.recent:
            if stimulus.source == 'Human':
                return False

        return True
    
    ...

def main():
    nessa_personality = ...
    Nessa = Puppy(nessa_personality)


    while True:
        if dt.now() - Nessa.time_reference_point > Nessa.clock:
            needs_report = Nessa.routine_checks()

            while True in needs_report.values()
                Nessa.squeak()
        
        else:
            Nessa.play()
