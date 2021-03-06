# Design-Pattern-Python
用Python实现23种设计模式

设计模式原则：
- 单一职责：就一个类而言，应该仅有一个引起它变化的原因
- 开放封闭：可以扩展，但是不可修改
- 依赖倒转：高层模块不应该依赖低层模块，二者都应该依赖于抽象；抽象不应该依赖细节，细节应该依赖抽象
- 里氏代换：子类型必须能够替换掉它们的父类型
- 合成聚合复用：尽量使用合成/聚合，尽量不要使用类继承
- 迪米特：如果两个类不必彼此直接通信，那么这两个类就不应当发生直接的相互作用，如果其中一个类需要调用另一个类的某一个方法的话，可以通过第三者转发这个调用

简单工厂模式不符合开放-封闭原则

- 创建型
  - 抽象工厂：提供一个创建一系列或相关依赖对象的接口，而无需指定它们具体的类
  - 建造者：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示
  - 工厂：定义一个用于创建对象的接口，让子类决定实例化哪一个类，将一个类的实例化延迟到子类
  - 原型：用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象
  - 单例模式：保证一个类仅有一个实例，并提供一个访问它的全局访问点
- 结构性
  - 适配器：将一个类的接口转换为客户希望的另一个接口，使得原本由于接口不兼容而不能工作的类可以一起工作
  - 桥接：将抽象部分与实现部分分离，使他们可以独立变化
  - 组合：将对象组合成树形结构以表示“部分-整体”的层次结构，组合模式使得用户对单个对象和组合对象的使用具有一致性
  - 装饰：动态地给一个对象添加一些额外的职责
  - 外观：为子系统中的一组接口提供一个一致的界面
  - 享元：运用共享技术有效地支持大量细粒度的对象
  - 代理：为其他对象提供一种代理以控制对这个对象的访问
- 行为型
  - 观察者：定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都得到通知并被自动更新
  - 模板：定义一个操作的算法骨架，而将一些步骤延迟到子类中，模板方法使得子类可以不改变一个算法打的结构即可重定义该算法的某些特性步骤
  - 命令：将一个请求封装成一个对象，从而使你可用不同的请求对客户进行参数化
  - 状态：允许一个对象在其内部状态改变时改变它的行为，让对象看起来似乎修改了它的类
  - 职责链：使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系，将这些对象连成一条链，并沿着这条链传递请求，直到有一个对象处理它为止
  - 解释器：给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子
  - 中介者：用一个中介对象来封装一系列的对象交互，中介者使各对象不需要显式地相互引用，从而使耦合松散，而且可以独立地改变它们之间的交互
  - 访问者：表示一个作用于某对象结构中的各元素的操作，它使你可以在不改变各元素的类的前提下定义作用于这些元素的操作
  - 策略：定义一系列的算法，把它们一个个封装起来，并使它们可以相互替换，使得算法可独立于使用它的客户而变化
  - 备忘录：在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态
  - 迭代器：提供一种方法顺序访问聚合对象中各个元素，而不暴露该对象的内部表示