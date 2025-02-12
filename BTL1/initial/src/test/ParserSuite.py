import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,301))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,302))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,303))
    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,304))
    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,305))
    #test variable declare
    def test_scalar_variable_declare1(self):
        input = """var i int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,306))
    def test_scalar_variable_declare2(self):
        input = """var i boolean;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,307))
    def test_scalar_variable_declare_with_struct_type(self):
        input = """var i foo;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,308))
    def test_scalar_variable_with_init(self):
        input = """var i int = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,309))
    def test_scalar_variable_missing_type(self):
        input = """var i = \"hello world\";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,310))
    def test_scalar_variable_missing_id(self):
        input = """var = 1;"""
        expect = "Error on line 1 col 5: ="
        self.assertTrue(TestParser.checkParser(input,expect,311))
    
    #constant declare
    def test_constant_declare(self):
        input = """const Pi = 3.14;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,312))
    def test_constant_declare_missing_id(self):
        input = """const = 3.14;"""
        expect = "Error on line 1 col 7: ="
        self.assertTrue(TestParser.checkParser(input,expect,313))
    def test_constant_declare_missing_value(self):
        input = """const Pi;"""
        expect = "Error on line 1 col 9: ;"
        self.assertTrue(TestParser.checkParser(input,expect,314))
    def test_constant_declare_missing_equal(self):
        input = """const Pi 3.14;"""
        expect = "Error on line 1 col 10: 3.14"
        self.assertTrue(TestParser.checkParser(input,expect,315))
    def test_constant_init_by_var(self):
        input = """const Pi = i;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,316))

    #array declare
    def test_array_declare_without_init(self):
        input = """var a [5] int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,317))
    def test_array_declare_without_init_many_dim(self):
        input = """var a [5][5][10][10] string;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,318))
    def test_array_declare_without_size(self):
        input = """var a [] int;"""
        expect = "Error on line 1 col 8: ]"
        self.assertTrue(TestParser.checkParser(input,expect,319))
    def test_array_declare_with_negative_size(self):
        input = """var a [-5] int;"""
        expect = "Error on line 1 col 8: -"
        self.assertTrue(TestParser.checkParser(input,expect,320))
    def test_array_declare_with_init(self):
        input = """var a [5] int = [5] int{1,2,3,4,5};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,321))
    def test_array_declare_with_init_and_many_dim(self):
        input = """var a [5][5][5] int = [5][5][5]int{
        {
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0}      },
        {
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0}        },
        {
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0}        },        {
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0}        },        {
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0}        }};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,322))
    def test_array_declare_with_init_not_enough_element(self):
        input = """var a [5] int = [5] int{1,2,3,4};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,323))
    def test_array_declare_with_init_too_many_element(self):
        input = """var a [5] int = [5] int{1,2,3,4,5,6};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,324))
    def test_array_declare_with_not_equal_dim(self):
        input = """var a [1][2] int = [2][1]int{{1},{2}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,325))
    def test_array_declare_with_not_enough_dim(self):
        input = """var a [1][2] int = [1]int{1};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,326))
    #struct declare
    def test_struct_declare(self):
        input = """type foo struct {
            a int;
            b float64;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,327))
    def test_struct_declare_missing_id(self):
        input = """type struct {
            a int;
            b float;
        };"""
        expect = "Error on line 1 col 6: struct"
        self.assertTrue(TestParser.checkParser(input,expect,328))
    def test_struct_declare_missing_semi(self):
        input = """type foo struct {
            a int;
            b float
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,329))
    def test_struct_declare_method_in_struct(self):
        input = """type foo struct {
            a int;
            b float;
            func main() {};
        };"""
        expect = "Error on line 4 col 13: func"
        self.assertTrue(TestParser.checkParser(input,expect,330))
    def test_use_instance_of_struct(self):
        input = """type student struct {
            name string;
            age int;
        };
        var s student = student{name: "Nguyen Van A",age: 20};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,331))
    def test_declare_struct_method(self):
        input = """func (s student) getAge() int {
            return s.age
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,332))
    def test_call_method_of_struct(self):
        input = """PutStringLn(s.getAge());"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,333))
    def test_nested_struct(self):
        input ="""type student struct{
            name string;
            age int;
            type address struct{
                street string;
                city string;
            };
        };"""
        expect = "Error on line 4 col 13: type"
        self.assertTrue(TestParser.checkParser(input,expect,334))
    #test interface declare
    def test_interface_declare(self):
        input = """type Calculator interface {
Add(x, y int) int;
Subtract(a, b float, c int) float;
Reset()
SayHello(name string)
};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,335))
    def test_interface_declare_missing_id(self):
        input = """type interface {
Add(x, y int) int;
Subtract(a, b float, c int) float;
Reset()
SayHello(name string)
};"""
        expect = "Error on line 1 col 6: interface"
        self.assertTrue(TestParser.checkParser(input,expect,336))
    
    #test function declare
    def test_function_declare(self):
        input = """func main() {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,337))
    def test_function_declare_with_param(self):
        input = """func main(a int, b float, c string) {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,338))
    def test_function_declare_with_return(self):
        input = """func main() int {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,339))
    def test_function_declare_with_param_and_return(self):
        input = """func main(a int, b float, c string) int {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,340))
    def test_function_declare_with_param_and_return_and_body(self):
        input = """func main(a int, b float, c string) int {
            return 1;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,341))
    def test_function_declare_with_param_sharing_same_type(self):
        input = """func main(a, b, c int) int {
            return 1;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,342))
    
    #test expression
    def test_complex_arithmetic_operators1(self):
        input = """func main() {
            a = b + c - d * e / f % g;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,343))    
    def test_complex_arithmetic_operators2(self):
        input = """func main() {
            a = b + c - d * e / f % g;
            b = a * c / d % e + f - g;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,344))
    def test_complex_arithmetic_operators3(self):
        input = """func main() {
            a = b + c - d * e / f % g;
            b = a * c / d % e + f - g;
            c = a + b + c + d + e;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,345))
    def test_complex_arithmetic_operators4(self):
        input = """func main() {
            a = a-b+c*d/e%f+g;
            b = d*e/f%g+a;
            c = e+ 2*f - 3/g + 4*h + 5+i;
            d = (a+b)*c/d;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,346))

    def test_relational_operators1(self):
        input = """func main() {
            bao = oba == boa;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,347))
    def test_relational_operators2(self):
        input = """func main() {
            bdh = sda != cdss;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,348))
    def test_relational_operators3(self):
        input =  """X = y >= z + 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,349))
    def test_relational_operators4(self):
        input =  """X = y <= z * 732004;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,350))
    def test_relational_operators5(self):
        input =  """X = y < z - 1505;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,351))
    def test_relational_operators6(self):
        input =  """X = y > z / 2225;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,352))
    def test_complex_relational_operators1(self):
        input = """check = GPA >= 3.5 && income < 7000000 || volunteer_hours > 30 && is_disabled;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,353))
    def test_complex_relational_operators2(self):
        input ="""cond = (price >= 1000000 && stock > 0) || (isSpecialItem == true && stock > 5);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,354))
    
    def test_negation_operators(self):
        input = """func main() {
            a = !b;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,355))
    def test_conjunction_operators(self):
        input = """func main() {
            a = b && c;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,356))

    def test_disjunction_operators(self):
        input = """func main() {
            a = b || c;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,357))

    def test_boolean_operators1(self):
        input = """func main() {
            ew = bn && mc || dl;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,358))
    def test_boolean_operators2(self):
        input = """func main(){
            woo = !!foo || !bar && !baz;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,359))
    def test_complex_boolean_operators1(self):
        input = """cond = n > 1 && (n % 2 != 0 || n == 2) && (n % 3 != 0 || n == 3) && (n % 5 != 0 || n == 5);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,360))
    def test_complex_boolean_operators2(self):
        input = """cond = (totalSpent > 5000000 && lastPurchaseDate <= 30) || (isVIP == true && referralCount >= 5);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,361))
    def test_complex_boolean_operators3(self):
        input = """cond = (age >= 18 && age <= 65) && (healthCondition == "good" || hasMedicalApproval == true);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,362))

    #test accessing element of array
    def test_access_array_element(self):
        input = """arr[1]= 2;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,363))
    def test_access_array_element_with_expression1(self):
        input = """arr[1+2*3]= 2;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,364))
    def test_access_array_element_with_expression2(self):
        input = """arr[-1--3]= 2+3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,365))
    def test_nested_access_array_element(self):
        input = """arr[arr[2]] = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,366))
    def test_array_access_with_variable(self):
        input = """arr[i] = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,367))
    def test_array_access_with_many_dim(self):
        input = """arr[1][2][3] = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,368))
    def test_many_dim_array_access_with_expression(self):
        input = """arr[1+2][2*3][3/4] = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,369))

    def test_struct_access_field(self):
        input = """s.name = "Nguyen Van A";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,370))
    def test_struct_deep_access_field(self):
        input = """s.info.id.address.street = "123 Nguyen";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,371))
    def test_struct_access_with_array_field(self):
        input = """s.info.id[2][s.info.id[1]] = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,372))
    def test_struct_access_with_expression(self):
        input = """s.info.id[2+3] = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,373))
    
    #test complex expressiion
    def test_complex_expression1(self):
        input = """c = ((a + b * c / d) % e == f) && ((g - h) * (i / j) >= k) || (!(m < n) && (o + p * q <= r)) && (s % t != 0 || u / v > w);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,374))
    def test_complex_expression2(self):
        input ="""b = ((a + b * c / (d - e) % f) == g || h * i - j / k >= l) && (!(m + n < o - p) || (q / r + s % t <= u)) && (v - w * x / y != z || (aa + bb * cc > dd && ee / ff <= gg)) || (!(hh % ii == 0) && jj * kk - ll / mm >= nn);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,375))
    def test_complex_expression3(self):
        input = """a = (((a * b + c / d - e % f) > g) && ((h + i * j - k / l) <= m) || (!(n - o < p * q) && (r % s != 0 || t / u >= v))) && (((w * x - y + z / aa) == bb) || ((cc % dd < ee && ff + gg >= hh) && (!(ii / jj > kk) || ll - mm * nn != oo)));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,376))
    def test_complex_expression4(self):
        input = """a = (((a + b * c / d - e % f) <= g || (h - i / j + k * l) > m) && (!(n % o == p) || (q / r - s + t * u != v))) || (((w + x - y * z / aa) >= bb && (cc % dd != ee || ff + gg / hh < ii)) && (!(jj - kk * ll > mm) || (nn / oo + pp - qq * rr <= ss)));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,377))
    def test_variable_declare_with_expression(self):
        input = """var i int = a+2*3/4%5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,378))
    def test_constant_declare_with_expression(self):
        input = """const P = 10+11/12-122*1223;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,379))
    def test_constant_declare_with_variable(self):
        input = """const P = (a+b*b)/a*b;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,380))
    def test_array_declare_with_expression_in_size(self):
        input = """var a [2+3] int;"""
        expect = "Error on line 1 col 9: +"
        self.assertTrue(TestParser.checkParser(input,expect,381))
    def test_array_declare_with_variable_in_size(self):
        input = """var a [b] int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,382))
    def test_struct_declare_with_array_field(self):
        input = """type student struct{
            name string;
            age int;
            scores [5] float;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,383)) 
    def test_struct_declare_with_init_in_field(self):
        input = """type student struct{
            name string;
            age int;
            scores [5] float = [5] float{1.0,2.0,3.0,4.0,5.0};
        };"""
        expect = "Error on line 4 col 30: ="
        self.assertTrue(TestParser.checkParser(input,expect,384))
    def test_array_access_in_complex_expression(self):
        input = """result = (((A[B[i] + C[j] * D[k] / E[l] - F[m] % G[n]] <= H[o] || I[P[Q[r]] - R[S[t]] / U[v] + W[x] * Y[z]] > J[aa]) && 
(!(K[L[M[p] % N[q]] == O[R[s]]) || (T[U[V[w] / X[y] - Z[bb] + CC[dd] * EE[ff]]] != FF[gg]))) || 
(((GG[HH[II[jj] - JJ[kk] * KK[ll] / LL[mm]]] + MM[NN[OO[pp]]]) >= PP[QQ[rr]] && 
(RR[SS[TT[uu] % UU[vv]] != VV[WW[xx]] || XX[YY[zz] + AAA[bbb] / BBB[ccc]] < CCC[DDD[eee]]))) && 
(!(EEE[FFF[GGG[hhh] - HHH[iii] * III[jjj] > JJJ[kkk]]] || KKK[LLL[MMM[nnn] / NNN[ooo] + OOO[ppp] - PPP[qqq] * QQQ[rrr]]] <= RRR[SSS[ttt]])));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,385))
    
    def test_struct_access_in_complex_expression(self):
        input = """result = (((s1.a + s2.b * s3.c / s4.d - s5.e % s6.f) <= s7.g || 
(s8.h - s9.i / s10.j + s11.k * s12.l) > s13.m) && 
(!(s14.n.p == s15.o.q) || 
(s16.r.s / s17.t.u - s18.v.w + s19.x.y * s20.z.aa != s21.bb.cc))) || 
(((s22.dd.ee - s23.ff.gg * s24.hh.ii / s25.jj.kk) >= s26.ll.mm && 
(s27.nn.oo % s28.pp.qq != s29.rr.ss || 
s30.tt.uu + s31.vv.ww / s32.xx.yy < s33.zz.aaa))) && 
(!(s34.bbb.ccc.ddd > s35.eee.fff.ggg) || 
(s36.hhh.iii.jjj / s37.kkk.lll.mmm + s38.nnn.ooo.ppp - 
s39.qqq.rrr.sss * s40.ttt.uuu.vvv <= s41.www.xxx.yyy));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 386))
    def test_struct_and_array_access_in_complex_expression(self):
        input = """result = (((s1.a[B[i] + s2.b * C[j] / s3.c - D[k] % s4.d] <= s5.e[F[m]] || 
(s6.f[G[n]] - s7.g / H[o] + s8.h * I[P[Q[r]]]) > s9.i[J[aa]] ) && 
(!(s10.j[K[L[M[p] % s11.k]] == s12.l[O[R[s]]]) || 
(s13.m[T[U[V[w] / X[y] - Z[bb] + s14.n.CC[dd] * EE[ff]]] != s15.o.FF[gg]))));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 387))
    
    def test_function_call_with_no_param(self):
        input = """func hello(){
        }
        hello();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 388))
    def test_function_call_with_param(self):
        input = """func hello(x ,y int, z int){
        }
        hello(1, 2 ,3);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 389))
    def test_function_call_with_expression_param(self):
        input = """func hello(x ,y int, z int){
        }
        hello(1+2, 3*4 ,5/6);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 390))
    def test_function_call_with_variable_param(self):
        input = """func hello(x ,y int, z int){
        }
        hello(a, b ,c);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 391))
    def test_function_call_with_array_param(self):
        input = """func hello(x ,y int, z int){
        }
        hello(a, b ,c[2]);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 392))
    def test_function_call_with_struct_param(self):
        input = """func hello(x ,y int, z int){
        }
        hello(a, b ,c.d);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 393))
    def test_function_call_with_other_function_call_param(self):
        input = """func hello(x ,y int, z int){
        }
        hello(a, b ,c(d));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 394))
    def test_function_call_with_missing_param(self):
        input = """func hello(x ,y int, z int){
        }
        hello(, a, b );"""
        expect = "Error on line 3 col 15: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 395))
    
    def test_method_call_with_no_param(self):
        input = """func (s student) hello(){
        }
        s.hello();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 396))
    def test_method_call_with_param(self):
        input = """func (s student) hello(x ,y int, z int){
        }
        s.hello(1, 2 ,3);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 397))
    def test_method_call_with_expression_param(self):
        input = """func (s student) hello(x ,y int, z int){
        }
        s.hello(1+2, 3*4 ,5/6);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 398))
    def test_method_call_with_variable_param(self):
        input = """func (s student) hello(x ,y int, z int){
        }
        s.hello(a, b ,c);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 399))
    def test_method_call_with_array_param(self):
        input = """func (s student) hello(x ,y int, z int){
        }
        s.hello(a, b ,c[2]);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 400))
    def test_method_call_with_struct_param(self):
        input = """func (s student) hello(x ,y int, z int){
        }
        s.hello(a, b ,c.d);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 401))
    def test_method_call_with_other_function_call_param(self):
        input = """func (s student) hello(x ,y int, z int){
        }
        s.hello(a, b ,c(d));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 402))
    def test_method_call_with_missing_param(self):
        input = """func (s student) hello(x ,y int, z int){
        }
        s.hello(, a, b );"""
        expect = "Error on line 3 col 17: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 403))
    def test_method_call_with_other_method_call_param(self):
        input = """func (s student) hello(x ,y int, z int){
        }
        s.hello(a, b ,c.d(e));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 404))

    #test asign statement
    def test_assign_statement1(self):
        input = """a = b+c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 405))
    def test_short_assign_statement(self):
        input = """a := d+12*4;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 406))
    def test_plus_assign_statement(self):
        input = """a += 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 407))
    def test_minus_assign_statement(self):
        input = """a -= a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 408))
    def test_mul_assign_statement(self):
        input = """a *= b;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 409))
    def test_div_assign_statement(self):
        input = """a /= bnf;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 410))
    def test_mod_assign_statement(self):
        input = """a %= bts;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 411))
    def test_assign_statement_with_array(self):
        input = """a[1] = 2;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 412))
    def test_assign_statement_with_struct(self):
        input = """s.name = "Nguyen Van A";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 413))

    #test if statement
    def test_if_statement(self):
        input = """if (yourAge >= 18){
            PutStringLn("You are an adult");
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 414))
    def test_if_statement_with_else(self):
        input = """if (yourAge >= 18){
            PutStringLn("You are an adult");
        } else {
            PutStringLn("You are a child");
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 415))
    def test_if_else_if_statement_not_else(self):
        input = """if (yourAge >= 18){
            PutStringLn("You are an adult");
        } else if (yourAge >= 12){
            PutStringLn("You are a teenager");
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 416))
    def test_if_else_if_statement_with_else(self):
        input = """if (yourAge >= 18){
            PutStringLn("You are an adult");
        } else if (yourAge >= 12){
            PutStringLn("You are a teenager");
        } else {
            PutStringLn("You are a child");
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 417))
    def test_nested_if_statement(self):
        input = """if (yourAge >= 18){
            if (yourAge >= 22){
                PutStringLn("You are a grown-up");
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 418))
    def test_nested_if_else_statement(self):
        input = """if (yourAge >= 18){
            if (yourAge >= 22){
                PutStringLn("You are a grown-up");
            } else {
                PutStringLn("You are an adult");
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 419))
    def test_nested_if_else_if_statement(self):
        input = """if (yourAge >= 18){
            if (yourAge >= 22){
                PutStringLn("You are a grown-up");
            } else if (yourAge >= 12){
                PutStringLn("You are a teenager");
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 420))
    def test_if_with_no_curly_brace(self):
        input = """if (yourAge >= 18)
            PutStringLn("You are an adult");"""
        expect = "Error on line 1 col 20: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 421))
    def test_if_with_no_condition(self):
        input = """if ()
            PutStringLn("You are an adult");"""
        expect = "Error on line 1 col 5: )"
        self.assertTrue(TestParser.checkParser(input, expect, 422))
    

    def test_029(self):
        input = """
        func (p Person) Greet() string {
            if (1) {return;}
            else if (1)
            {}
        };"""
        expect = "Error on line 4 col 16: else"
        self.assertTrue(TestParser.checkParser(input ,expect, 423))
# #khai báo hàm lồng hàm thì sao
#     #test lại các declare với expr *
#     #test khai báo mảng với expression là size *
#     #test khai báo struct với field là array *
#     #test nhét array vào paramlist được hay không
    
