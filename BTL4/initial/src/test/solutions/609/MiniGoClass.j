.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is car LCar; from Label2 to Label3
	new Car
	dup
	invokespecial Car/<init>()V
	dup
	iconst_4
	anewarray Wheel
	dup
	iconst_0
	new Wheel
	dup
	invokespecial Wheel/<init>()V
	dup
	ldc "Michelin"
	putfield Wheel/brand Ljava/lang/String;
	aastore
	dup
	iconst_1
	new Wheel
	dup
	invokespecial Wheel/<init>()V
	dup
	ldc "Bridgestone"
	putfield Wheel/brand Ljava/lang/String;
	aastore
	dup
	iconst_2
	new Wheel
	dup
	invokespecial Wheel/<init>()V
	dup
	ldc "Goodyear"
	putfield Wheel/brand Ljava/lang/String;
	aastore
	dup
	iconst_3
	new Wheel
	dup
	invokespecial Wheel/<init>()V
	dup
	ldc "Dunlop"
	putfield Wheel/brand Ljava/lang/String;
	aastore
	putfield Car/wheel [LWheel;
	astore_1
	aload_1
	getfield Car/wheel [LWheel;
	iconst_0
	aaload
	ldc "Michelin"
	putfield Wheel/brand Ljava/lang/String;
	aload_1
	getfield Car/wheel [LWheel;
	iconst_0
	aaload
	getfield Wheel/brand Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label3:
	nop
Label1:
	return
.limit stack 8
.limit locals 2
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
