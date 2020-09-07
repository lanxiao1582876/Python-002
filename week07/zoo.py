from abc import ABCMeta, abstractmethod
class Animal(metaclass=ABCMeta):
    def __init__(self, atype, Bodytype, character, ferocious):
          self.atype = atype
          self.Bodytype = Bodytype
          self.character = character
          self.ferocious = ferocious
    
    @abstractmethod
    def  is_ferocious(self, tpye, Bodytype, character):
         pass

class Cat(Animal):
    sound = 'miao'  

    def __init__(self, atype, Bodytype, character, ferocious):
          super().__init__(atype, Bodytype, character, ferocious)
    
    @property
    def  is_ferocious(self, tpye, Bodytype, character):
          size_dict = {'大型':3, '中等':2, '小型':1 }
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

    def __init__(self, atype, Bodytype, character, ferocious):
          super().__init__(atype, Bodytype, character, ferocious)
    
    @property
    def  is_ferocious(self, tpye, Bodytype, character):
          size_dict = {'大型':3, '中等':2 ,'小型':1 }
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
      def __init__(self, name, alist=None):
            self.name = name 
            if alist is None:
                self.alist = []
      
      def add_animal(self,animal):
            setattr(self,animal.__class__.__name__,animal)
            if animal not in self.alist:
                  self.alist.append(animal)
            else:
                  print(f"{animal.__dict__['name']}已存在,不需再添加")

               

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫', '食肉', '小', '温顺')
    # 实例化狗，属性包括名字、类型、体型、性格
    dog1 = Dog('小金毛', '杂食', '中', '温顺')
    # 增加一只只猫和一只狗到动物园
    z.add_animal(cat1)
    #z1.add_animal(cat1)
    z.add_animal(dog1)

    # 动物园是有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(have_cat)
