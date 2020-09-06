from zoo_calss import ABCMeta, abstractmethod
class Animal(metaclass=ABCMeta):
    def __init__(self, type, Bodytype, character, ferocious):
          self.type = a_type
          self.Bodytype = Bodytype
          self.character = character
          self.ferocious = ferocious
    
    @abstractmethod
    def  is_ferocious(self, tpye, Bodytype, character):
         pass

class Cat(Animal):
    sound = 'miao'  

    def __init__(self, type, Bodytype, character, ferocious):
          super().__init__(self, type, Bodytype, character, ferocious)
    
    @property
    def  is_ferocious(self, tpye, Bodytype, character):
          size_dict = {'大型':3, '中等':2 '小型':1 }
          if self.type == "食肉" and self.Bodytype >=2 and self.character == "凶猛":
                return True
          else:
                return False
    
     @property
     def is_pet(self):
           if self.is_ferocious:
                 return "不适合宠物"
            else:
                  return "适合做宠物"
              


class Dog(Animal):
    sound = 'wang'  

    def __init__(self, type, Bodytype, character, ferocious):
          super().__init__(self, type, Bodytype, character, ferocious)
    
    @property
    def  is_ferocious(self, tpye, Bodytype, character):
          size_dict = {'大型':3, '中等':2 '小型':1 }
          if self.type == "食肉" and self.Bodytype >=2 and self.character == "凶猛":
                return True
          else:
                return False
    
     @property
     def is_pet(self):
           if self.is_ferocious:
                 return "不适合宠物"
            else:
                  return "适合做宠物"

class Zoo():
      def __init__(self, name):
            self.name = name 
            self.animals = {}
      
      def add_animal(self,animal):
            animal_cls_name = animal.__class__.__name__
            if animal_cls_name in self.animals:
                  for i in self.animals[animal_cls_name]:
                        if animal is i:
                              return None
                  self.animals[animal_cls_name].append(animal)
            else:
                  self.animals[animal_cls_name] = [animal]
                  setattr(self, animal_cls_name, 'have')

if __name__ == '__main__':
    # 实例化动物园
    z1 = Zoo('时间动物园')
    z2 = Zoo('欢乐动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    cat2 = Cat('小黑猫', '食肉', '小', '温顺')
    cat3 = Cat('狸花猫', '食肉', '小', '凶猛')
    # 实例化两只狗，属性包括名字、类型、体型、性格
    dog1 = Dog('小金毛', '杂食', '中', '温顺')
    dog2 = Dog('田园犬', '杂食', '小', '凶猛')
    # 增加两只猫和一只狗到动物园1
    z1.add_animal(cat1)
    z1.add_animal(cat1)
    z1.add_animal(cat2)
    z1.add_animal(dog1)
    # 增加一只猫和一只狗到动物园2
    z2.add_animal(cat3)
    z2.add_animal(dog2)
    # 动物园1是否有猫这种动物
    have_cat = hasattr(z1, 'Cat')
    print(have_cat)
    # 动物园2是否有狗这种动物
    have_dog = hasattr(z2, 'Dog')
    print(have_dog)

    # 凶猛动物
    cat007 = Cat('黑猫', '食肉', '中等', '凶猛')
    print("凶猛动物：", cat007.is_ferocious)
    print("宠物：", cat007.is_pet)
    cat008 = Cat('白猫', '食肉', '大', '温顺')
    print("凶猛动物：", cat008.is_ferocious)
    print("宠物：", cat008.is_pet)



if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
