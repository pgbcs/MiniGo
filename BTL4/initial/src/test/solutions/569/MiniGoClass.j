.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static foo(Ljava/lang/String;)V
.var 0 is a Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	dup
	aload_0
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	dup
	ldc " world"
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	astore_0
Label3:
	nop
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a Ljava/lang/String; from Label2 to Label3
	ldc "hello"
	astore_1
	aload_1
	invokestatic MiniGoClass/foo(Ljava/lang/String;)V
	aload_1
	invokestatic io/putString(Ljava/lang/String;)V
Label3:
	nop
Label1:
	return
.limit stack 1
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
