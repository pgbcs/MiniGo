.source Circle.java
.class public Circle
.super java.lang.Object
.implements Shape
.field radius F

.method public <init>()V
.var 0 is this LCircle; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	ldc 0.0
	putfield Circle/radius F
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public area()F
.var 0 is this LCircle; from Label0 to Label1
Label0:
Label2:
	ldc 3.14
	aload_0
	getfield Circle/radius F
	fmul
	aload_0
	getfield Circle/radius F
	fmul
	freturn
Label3:
	nop
Label1:
.limit stack 5
.limit locals 1
.end method
