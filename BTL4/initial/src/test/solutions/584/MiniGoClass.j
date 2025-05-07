.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static isEven(I)Z
.var 0 is n I from Label0 to Label1
Label0:
Label2:
	iload_0
	iconst_2
	irem
	iconst_0
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ireturn
Label3:
	nop
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a I from Label2 to Label3
	iconst_5
	istore_1
.var 2 is b I from Label2 to Label3
	bipush 10
	istore_2
.var 3 is c Z from Label2 to Label3
	iload_1
	invokestatic MiniGoClass/isEven(I)Z
	istore_3
	iload_3
	invokestatic io/putBoolLn(Z)V
	iload_2
	invokestatic MiniGoClass/isEven(I)Z
	invokestatic io/putBoolLn(Z)V
	iconst_3
	invokestatic MiniGoClass/isEven(I)Z
	ifle Label4
	iconst_4
	invokestatic MiniGoClass/isEven(I)Z
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBoolLn(Z)V
Label3:
	nop
Label1:
	return
.limit stack 2
.limit locals 4
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
