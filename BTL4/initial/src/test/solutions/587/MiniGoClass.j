.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static createCircle(F)LShape;
.var 0 is radius F from Label0 to Label1
Label0:
Label2:
	new Circle
	dup
	invokespecial Circle/<init>()V
	dup
	fload_0
	putfield Circle/radius F
	areturn
Label3:
	nop
Label1:
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is c LShape; from Label2 to Label3
	ldc 5.0
	invokestatic MiniGoClass/createCircle(F)LShape;
	astore_1
	aload_1
	invokeinterface Shape/area()F 1
	invokestatic io/putFloatLn(F)V
Label3:
	nop
Label1:
	return
.limit stack 1
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
