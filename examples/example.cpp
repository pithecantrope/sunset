#include <iostream>

template <typename T>
class Box {
        T value;
    public:
        Box(T val) : value(val) {}
        T getValue() const { return value; }
        void setValue(T val) { value = val; }
        void print() const { std::cout << "Value: " << value << std::endl; }
};

template <typename T>
void printBox(const Box<T>& box) { box.print(); }

int main() {
        Box<int> intBox(42);
        Box<std::string> strBox("Hello");
        intBox.print();
        strBox.print();
        intBox.setValue(100);
        printBox(intBox);

        return 0;
}
