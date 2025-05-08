.source Point.java
.class public Point
.super java.lang.Object
.field x I
.field y I

.method public <init>()V
.var 0 is this LPoint; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_0
	putfield Point/x I
	aload_0
	iconst_0
	putfield Point/y I
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public distance()I
.var 0 is this LPoint; from Label0 to Label1
Label0:
Label2:
	aload_0
	getstatic MiniGoClass/X I
	invokevirtual Point/setX(I)V
	aload_0
	getstatic MiniGoClass/Y I
	invokevirtual Point/setY(I)V
	getstatic MiniGoClass/X I
	getstatic MiniGoClass/Y I
	invokestatic MiniGoClass/calculateDistance(II)I
	ireturn
Label3:
	nop
Label1:
.limit stack 4
.limit locals 1
.end method

.method public setX(I)V
.var 0 is this LPoint; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
Label2:
	aload_0
	iload_1
	putfield Point/x I
Label3:
	nop
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public setY(I)V
.var 0 is this LPoint; from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
Label2:
	aload_0
	iload_1
	putfield Point/y I
Label3:
	nop
Label1:
	return
.limit stack 2
.limit locals 2
.end method
