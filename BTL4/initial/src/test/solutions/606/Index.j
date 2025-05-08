.source Index.java
.class public Index
.super java.lang.Object
.field value I

.method public <init>()V
.var 0 is this LIndex; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_0
	putfield Index/value I
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public getValue(I)I
.var 0 is this LIndex; from Label0 to Label1
.var 1 is off I from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Index/value I
	iload_1
	iadd
	ireturn
Label3:
	nop
Label1:
.limit stack 3
.limit locals 2
.end method
