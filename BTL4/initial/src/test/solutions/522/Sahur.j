.source Sahur.java
.class public Sahur
.super java.lang.Object
.field value I

.method public Add(I)V
.var 0 is this LSahur; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Sahur/value I
	iload_1
	iadd
	aload_0
	putfield Sahur/value I
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LSahur; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
