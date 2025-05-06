.source Student.java
.class public Student
.super java.lang.Object
.field name Ljava/lang/String;
.field age I

.method public <init>()V
.var 0 is this LStudent; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aconst_null
	putfield Student/name Ljava/lang/String;
	aload_0
	iconst_0
	putfield Student/age I
Label1:
	return
.limit stack 2
.limit locals 1
.end method
