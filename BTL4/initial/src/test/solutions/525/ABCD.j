.source ABCD.java
.class public ABCD
.super java.lang.Object
.field value I

.method public Add(I)I
.var 0 is this LABCD; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
Label2:
	aload_0
	aload_0
	getfield ABCD/value I
	iload_1
	iadd
	putfield ABCD/value I
	aload_0
	getfield ABCD/value I
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LABCD; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
