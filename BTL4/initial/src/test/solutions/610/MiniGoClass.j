.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is b I from Label2 to Label3
	iconst_1
	istore_1
.var 2 is car LCar; from Label2 to Label3
	new Car
	dup
	invokespecial Car/<init>()V
	dup
	iconst_4
	iconst_2
	multianewarray [[LWheel; 2
	dup
	iconst_0
	aaload
	iconst_0
	new Wheel
	dup
	invokespecial Wheel/<init>()V
	dup
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Michelin"
	aastore
	dup
	iconst_1
	ldc "Br Br"
	aastore
	putfield Wheel/brand [Ljava/lang/String;
	aastore
	dup
	iconst_0
	aaload
	iconst_1
	new Wheel
	dup
	invokespecial Wheel/<init>()V
	dup
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Bridgestone"
	aastore
	dup
	iconst_1
	ldc "Hmmm"
	aastore
	putfield Wheel/brand [Ljava/lang/String;
	aastore
	dup
	iconst_1
	aaload
	iconst_0
	new Wheel
	dup
	invokespecial Wheel/<init>()V
	dup
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Goodyear"
	aastore
	dup
	iconst_1
	ldc "GoodLife"
	aastore
	putfield Wheel/brand [Ljava/lang/String;
	aastore
	dup
	iconst_1
	aaload
	iconst_1
	new Wheel
	dup
	invokespecial Wheel/<init>()V
	dup
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Dunlop"
	aastore
	dup
	iconst_1
	ldc "Jumbo"
	aastore
	putfield Wheel/brand [Ljava/lang/String;
	aastore
	dup
	iconst_2
	aaload
	iconst_0
	new Wheel
	dup
	invokespecial Wheel/<init>()V
	dup
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Pirelli"
	aastore
	dup
	iconst_1
	ldc "TungTungSahur"
	aastore
	putfield Wheel/brand [Ljava/lang/String;
	aastore
	dup
	iconst_2
	aaload
	iconst_1
	new Wheel
	dup
	invokespecial Wheel/<init>()V
	dup
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Continental"
	aastore
	dup
	iconst_1
	ldc "Bruh"
	aastore
	putfield Wheel/brand [Ljava/lang/String;
	aastore
	dup
	iconst_3
	aaload
	iconst_0
	new Wheel
	dup
	invokespecial Wheel/<init>()V
	dup
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Hankook"
	aastore
	dup
	iconst_1
	ldc "Boa"
	aastore
	putfield Wheel/brand [Ljava/lang/String;
	aastore
	dup
	iconst_3
	aaload
	iconst_1
	new Wheel
	dup
	invokespecial Wheel/<init>()V
	dup
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Toyo"
	aastore
	dup
	iconst_1
	ldc "ta"
	aastore
	putfield Wheel/brand [Ljava/lang/String;
	aastore
	putfield Car/wheel [[LWheel;
	astore_2
	aload_2
	getfield Car/wheel [[LWheel;
	iconst_0
	aaload
	iload_1
	aaload
	getfield Wheel/brand [Ljava/lang/String;
	iconst_1
	ldc "Bridgestone"
	aastore
	aload_2
	getfield Car/wheel [[LWheel;
	iconst_0
	aaload
	iconst_1
	aaload
	getfield Wheel/brand [Ljava/lang/String;
	iconst_0
	aaload
	invokestatic io/putString(Ljava/lang/String;)V
Label3:
	nop
Label1:
	return
.limit stack 12
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
