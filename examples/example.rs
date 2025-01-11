struct Person {
        name: String,
        age: u8,
}

impl Person {
        fn new(name: String, age: u8) -> Self {
                Person { name, age }
        }
        fn greet(&self) -> String {
                format!("Hello, my name is {} and I am {} years old.", self.name, self.age)
        }
        fn birthday(&mut self) {
                self.age += 1;
                println!("Happy birthday, {}! You are now {}.", self.name, self.age);
        }
}

fn main() {
        let mut person = Person::new(String::from("Alice"), 30);
        println!("{}", person.greet());
        person.birthday();
        println!("{}", person.greet());
}
