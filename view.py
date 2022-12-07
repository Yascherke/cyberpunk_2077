from mongodb import Finder
from update import updateRank
from system import catchSkill
from programs import Interface
from roles import Role

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
        role = finder.skills()
        rank = finder.ranks(gen_info[2])
        status = finder.status()
        updateRank(self.uid)
        text = f"""
------------------------------------------------
    {role[4]} {gen_info[0]}

    Известность: {rank[0]}
    Очки известности: {gen_info[3]}

    Здоровье: {hp[1]} из {hp[0]}
    Тяжёлое ранение: {hp[2]}
    Испытание смерти: {hp[3]}

    Корпорация: {other[1]}
    Банда: {other[0]}
    Организация: {other[2]}

    Trauma Team: {status[3]}

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
                Иммущество

    Слот 1: {bp[0]}
    Слот 2: {bp[1]}
    Слот 3: {bp[2]}
    Слот 4: {bp[3]}
    Слот 5: {bp[4]}
    Слот 6: {bp[5]}
    Слот 7: {bp[6]}
    Слот 8: {bp[7]}
    Слот 9: {bp[8]}
    Слот 10: {bp[9]}
    Слот 11: {bp[5]}
    Слот 12: {bp[6]}
    Слот 13: {bp[7]}
    Слот 14: {bp[8]}
    Слот 15: {bp[9]}
------------------------------------------------
    
    Дом: {house[0]}
    Машина: {car[0]}
------------------------------------------------
    """
        return text

    def myEquip(self):
        finder = Finder(self.uid)
        equip = finder.equipment()
        magazine = finder.magazine()
        ammo = finder.ammo()
        mods = finder.weapMods()

        text = f"""
------------------------------------------------
                    Экипировка

    Оружие: {equip[0]}
    Магазин: {magazine[0]} из {magazine[1]}
    Типо боеприпасов: {ammo[13]}

    Обвесы:
    Магазан: {mods[0]}
    Прицел: {mods[1]}
    Коннектор: {mods[3]}
    Насадка: {mods[2]}

    Защита: {equip[1]} | {equip[2]}


    Количество магазинов:

    Стандартные: {ammo[0]}
    Бронебойные: {ammo[1]}
    Биотоксин: {ammo[2]}
    ЭМИ: {ammo[3]}
    Экспансивные: {ammo[4]}
    Светошумовые: {ammo[5]}
    Зажигательные: {ammo[6]}
    Ядовитые: {ammo[7]}
    Резиновые: {ammo[8]}
    Усыпляющие: {ammo[9]}
    Умные: {ammo[10]}
    Дымовые(гранаты): {ammo[11]}
    Слезоточивый газ(гранаты): {ammo[12]}
    Ракеты: {ammo[14]}
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

    def netrunner(self):
        finder = Finder(self.uid)
        bp = finder.nrPrograms()
        equip = finder.nrEquip()
        inter = Interface(self.uid)
        inter.lvlUp()
        inter.updateAction()
        deka = finder.getNRunner()
        text = f"""
------------------------------------------------
                ИНТЕРФЕЙС
------------------------------------------------
                {deka[5]}

    Программа 1: {bp[0]}
    Программа 2: {bp[1]}
    Программа 3: {bp[2]}
    Программа 4: {bp[3]}
    Программа 5: {bp[4]}
    Программа 6: {bp[5]}
    Программа 7: {bp[6]}
    Программа 8: {bp[7]}
    Программа 9: {bp[8]}
    Программа 10: {bp[9]}
    Программа 11: {bp[10]}
    Программа 12: {bp[11]}
    Программа 13: {bp[12]}
    Программа 14: {bp[13]}
    Программа 15: {bp[14]}

********************************

    Оборудывание 1: {equip[0]}
    Оборудывание 2: {equip[1]}
    Оборудывание 3: {equip[2]}
    Оборудывание 4: {equip[3]}
    Оборудывание 5: {equip[4]}
    Оборудывание 6: {equip[5]}
    Оборудывание 7: {equip[6]}
    Оборудывание 8: {equip[7]}
    Оборудывание 9: {equip[8]}
    Оборудывание 10: {equip[9]}

------------------------------------------------
    
    Ранг навыка: {deka[2]}
    Опыт: {deka[3]}

    Действий в системе: {deka[4]}  
------------------------------------------------
    """
        return text
    
    def rockeboy(self):
        finder = Finder(self.uid)
        rocker = Role(self.uid)
        rocker.rocker()
        info = finder.rockerboy()
        text = f"""
------------------------------------------------
                ХАРИЗМА
------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text

    def solo(self):
        finder = Finder(self.uid)
        rocker = Role(self.uid)
        rocker.solo()
        info = finder.solo()
        text = f"""
------------------------------------------------
                БОЕВОЕ ЧУТЬЁ
------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text
    
    def media(self):
        finder = Finder(self.uid)
        rocker = Role(self.uid)
        rocker.media()
        info = finder.media()
        text = f"""
------------------------------------------------
                ДОВЕРИЕ
------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text

    def police(self):
        finder = Finder(self.uid)
        rocker = Role(self.uid)
        rocker.police()
        info = finder.police()
        text = f"""
------------------------------------------------
                ПОДКРЕПЛЕНИЕ
------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text
    
    def fixer(self):
        finder = Finder(self.uid)
        rocker = Role(self.uid)
        rocker.fixer()
        info = finder.fixer()
        text = f"""
------------------------------------------------
                ВОРОТИЛА
------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text
    
    def ekzek(self):
        finder = Finder(self.uid)
        rocker = Role(self.uid)
        rocker.ekzek()
        info = finder.ekzek()
        text = f"""
------------------------------------------------
                КОМАНДНАЯ РАБОТА
------------------------------------------------

    Подчиненный: {info[4]}
    Подчиненный: {info[5]}
    Подчиненный: {info[6]}

------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text

    def nomad(self):
        finder = Finder(self.uid)
        rocker = Role(self.uid)
        rocker.nomad()
        info = finder.nomad()
        text = f"""
------------------------------------------------
                МОТО
------------------------------------------------
            Гараж Семьи

    Машина 1-4 ранг: {info[4]}
    Машина 5-6 ранг: {info[5]}
    Машина 7-8 ранг: {info[6]}
    Машина 9-10 ранг: {info[7]}

    Машина 1-4 ранг(улучшения): {info[8]}
    Машина 5-6 ранг(улучшения): {info[9]}
    Машина 7-8 ранг(улучшения): {info[10]}
    Машина 9-10 ранг(улучшения): {info[11]}
------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text

    def tech(self):
        finder = Finder(self.uid)
        rocker = Role(self.uid)
        rocker.tech()
        info = finder.tech()
        text = f"""
------------------------------------------------
                СОЗДАТЕЛЬ
------------------------------------------------

    Свободные очки: {info[4]}
    
    Мастер модернизации: {info[5]}
    Мастер модернизации: {info[6]}
    Мастер модернизации: {info[7]}

------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text
    
    def reaper(self):
        finder = Finder(self.uid)
        rocker = Role(self.uid)
        rocker.reaper()
        info = finder.reaper()
        text = f"""
------------------------------------------------
                Медицина
------------------------------------------------

    Свободные очки: {info[4]}
    
    Хирургия: {info[5]}
    МедТех(Фармацевтика): {info[6]}
    МедТех(Криосистемы): {info[7]}

------------------------------------------------
    
    Ранг навыка: {info[2]}
    Опыт: {info[3]}
 
------------------------------------------------
    """
        return text

    def implants(self):
        find = Finder(self.uid)
        audio = find.audio()
        reye = find.right_eye()
        leye = find.left_eye()
        rarm = find.right_arm()
        larm = find.left_arm()
        rleg = find.right_leg()
        lleg = find.left_leg()
        neural = find.neural()
        inside = find.inside()
        outside = find.outside()
        style = find.style()
        borg = find.borg()

        text = f"""
------------------------------------------------
                    Импланты

    Аудио разьем: {audio[0]}
    Слот 1: {audio[1]}
    Слот 2: {audio[2]}
    Слот 3: {audio[3]}

    Правый глаз: {reye[0]}
    Слот 1: {reye[1]}
    Слот 2: {reye[2]}
    Слот 3: {reye[3]}

    Левый глаз: {leye[0]}
    Слот 1: {leye[1]}
    Слот 2: {leye[2]}
    Слот 3: {leye[3]}

    Нейроинтерфейс: {neural[0]}
    Слот 1: {neural[1]}
    Слот 2: {neural[2]}
    Слот 3: {neural[3]}
    Слот 4: {neural[4]}
    Слот 5: {neural[5]}

    Правая рука: {rarm[0]}
    Слот 1: {rarm[1]}
    Слот 2: {rarm[2]}
    Слот 3: {rarm[3]}
    Слот 4: {rarm[4]}


    Левая рука: {larm[0]}
    Слот 1: {larm[1]}
    Слот 2: {larm[2]}
    Слот 3: {larm[3]}
    Слот 4: {larm[4]}

    
    Правая нога: {rleg[0]}
    Слот 1: {rleg[1]}
    Слот 2: {rleg[2]}
    Слот 3: {rleg[3]}


    Левая нога: {lleg[0]}
    Слот 1: {lleg[1]}
    Слот 2: {lleg[2]}
    Слот 3: {lleg[3]}
  

    Внутр. импланты:
    Слот 1: {inside[0]}
    Слот 2: {inside[1]}
    Слот 3: {inside[2]}
    Слот 4: {inside[3]}
    Слот 5: {inside[4]}
    Слот 6: {inside[5]} 
    Слот 7: {inside[6]}

    Внешние импланты:
    Слот 1: {outside[0]}
    Слот 2: {outside[1]}
    Слот 3: {outside[2]}
    Слот 4: {outside[3]}
    Слот 5: {outside[4]}
    Слот 6: {outside[5]}
    Слот 7: {outside[6]}


    Стилевые импланты:
    Слот 1: {style[0]}
    Слот 2: {style[1]}
    Слот 3: {style[2]}
    Слот 4: {style[3]}
    Слот 5: {style[4]}
    Слот 6: {style[5]}
    Слот 7: {style[6]}


    Боргирование:
    Слот 1: {borg[0]}
    Слот 2: {borg[1]}
    Слот 3: {borg[2]}
    Слот 4: {borg[3]}
    Слот 5: {borg[4]}
    Слот 6: {borg[5]}
    Слот 7: {borg[6]}

------------------------------------------------
        """
        return text