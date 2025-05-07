.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static add(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
Label2:
	iload_0
	iload_1
	iadd
	ireturn
Label3:
	nop
Label1:
.limit stack 2
.limit locals 2
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
.var 3 is c I from Label2 to Label3
	iload_1
	iload_2
	invokestatic MiniGoClass/add(II)I
	istore_3
	iload_3
	invokestatic io/putInt(I)V
	iconst_3
	iconst_4
	invokestatic MiniGoClass/add(II)I
	invokestatic io/putInt(I)V
	iconst_1
	iconst_2
	invokestatic MiniGoClass/add(II)I
	iconst_3
	iconst_4
	invokestatic MiniGoClass/add(II)I
	iadd
	invokestatic io/putInt(I)V
	iconst_1
	iconst_2
	invokestatic MiniGoClass/add(II)I
	iconst_3
	iconst_4
	invokestatic MiniGoClass/add(II)I
	invokestatic MiniGoClass/add(II)I
	invokestatic io/putInt(I)V
Label3:
	nop
Label1:
	return
.limit stack 3
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
