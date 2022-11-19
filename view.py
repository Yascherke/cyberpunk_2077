from mongodb import Finder
from update import updateRank
from system import catchSkill

class View:

    def __init__(self, uid):
        self.uid = uid

    def myStats(self):
        finder = Finder(self.uid)
        stats = finder.stats()
        skills = finder.skills()
        text = f"""
------------------------------------------------
            Характеристики

    Интеллект: {stats[0]}
    Реакция: {stats[1]}
    Ловкость: {stats[2]}
    Техника: {stats[3]}
    Крутость: {stats[4]}
    Воля: {stats[5]}
    Удача: {stats[6]}
    Скорость: {stats[7]}
    Телосложение: {stats[8]}
    Эмпатия: {stats[9]}

    Человечность: {skills[3]} из 100
------------------------------------------------
    """
        return text

    def myProfile(self):
        finder = Finder(self.uid)
        gen_info = finder.generalInfo()
        money = finder.money()
        hp = finder.hpInfo()
        other = finder.otherInfo()
        role = finder.roles(gen_info[1])
        rank = finder.ranks(gen_info[2])
        updateRank(self.uid)
        text = f"""
------------------------------------------------
    {role} {gen_info[0]}

    Известность: {rank[0]}
    Очки известности: {gen_info[3]}

    Здоровье: {hp[1]} из {hp[0]}
    Тяжёлое ранение: {hp[2]}
    Испытание смерти: {hp[3]}

    Корпорация: {other[1]}
    Банда: {other[0]}

    Евродоллары: {money}
------------------------------------------------
    """
        return text

    def myProperty(self):
        finder = Finder(self.uid)
        geninf = finder.generalInfo()
        bp = finder.backpack()
        car = finder.cars(geninf[4])
        house = finder.cars(geninf[5])

        text = f"""
------------------------------------------------
                Карманы

    Слот 1: {bp[0]}
    Слот 2: {bp[1]}
    Слот 3: {bp[2]}
    Слот 4: {bp[3]}
    Слот 5: {bp[4]}
    Слот 6: {bp[5]}
    Слот 7: {bp[6]}
    Слот 8: {bp[7]}
    Слот 9: {bp[6]}
    Слот 10: {bp[7]}
------------------------------------------------
    
    Дом: {house[0]}
    Машина: {car[0]}
------------------------------------------------
    """
        return text

    def myEquip(self):
        finder = Finder(self.uid)
        skills = finder.skills()
        equip = finder.equipment()

        text = f"""
------------------------------------------------
                    Экипировка

        Оружие: {equip[0]}

        Защита головы: {equip[1]} | {equip[2]}

------------------------------------------------
        
        Импланты: {skills[1]}
        Программы: {skills[2]}
------------------------------------------------
        """
        return text

    def mySkills(self):
        
        catch = catchSkill(self.uid)
        def slist(prop):
            text = ''
            for x in prop:
                text += f"""{x}\n\n"""
            return text
        text = f"""
------------------------------------------------
                    Навыки

{slist(catch)}           
------------------------------------------------
        """
        return text