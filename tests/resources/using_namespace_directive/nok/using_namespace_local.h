#ifndef FOO_BAR_H_
#define FOO_BAR_H_

#include <map>
#include <string>


namespace foo {

struct Qux {
    using namespace std;
    map<int, string> foo;
};

} // namespace foo

#endif /* FOO_BAR_H_ */
