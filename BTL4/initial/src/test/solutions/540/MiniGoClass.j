.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static foo()I
Label0:
Label2:
	iconst_1
	ireturn
.var 0 is a I from Label2 to Label3
	iconst_2
	istore_0
	iload_0
	ireturn
Label3:
	nop
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	invokestatic MiniGoClass/foo()I
	invokestatic io/putInt(I)V
Label3:
	nop
Label1:
	return
.limit stack 1
.limit locals 1
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
