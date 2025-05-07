.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static greet(Ljava/lang/String;)Ljava/lang/String;
.var 0 is name Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	ldc "Hello, "
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	aload_0
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	ldc "!"
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	areturn
Label3:
	nop
Label1:
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a Ljava/lang/String; from Label2 to Label3
	ldc "Alice"
	astore_1
.var 2 is b Ljava/lang/String; from Label2 to Label3
	aload_1
	invokestatic MiniGoClass/greet(Ljava/lang/String;)Ljava/lang/String;
	astore_2
	aload_2
	invokestatic io/putStringLn(Ljava/lang/String;)V
	ldc "Bob"
	invokestatic MiniGoClass/greet(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	ldc "Charlie"
	invokestatic MiniGoClass/greet(Ljava/lang/String;)Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	ldc " "
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	ldc "Dave"
	invokestatic MiniGoClass/greet(Ljava/lang/String;)Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
	nop
Label1:
	return
.limit stack 3
.limit locals 3
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
