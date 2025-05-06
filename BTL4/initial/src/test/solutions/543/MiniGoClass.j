.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is i I from Label2 to Label3
	iconst_0
	istore_1
Label6:
	iload_1
	bipush 10
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	iload_1
	invokestatic io/putInt(I)V
Label10:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label6
Label5:
Label3:
	nop
Label1:
	return
.limit stack 2
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
