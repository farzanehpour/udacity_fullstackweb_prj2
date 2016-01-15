#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
# This file has been updated by Shiva Farzanehpour (farzanehpour@gmail.com)
# for Udacity full stack web development.
#

import psycopg2
import traceback
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("delete from matches;")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("delete from players;")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("select count(id) from players;")
    numOfPlayers = cursor.fetchone()
    db.close()
    return numOfPlayers[0]


def registerTournament(id, name):
    """ Register a new Tournament.

    This table keeps tracks of tournaments in case that more than one
    tournament is running at the same time.

    Args:
    id : Unique identifier of each tournament.
    name : Tournament name (i.e. "Campus A chess tournament").

    Returns:
        if tournament registered successfully, prints out succeful message :
        "Tournament {Tournament name} is successfully registered."

        In case of error during registration, it reflects DB message on
        console.
     """
    if id < 1:
        raise ValueError("Tournament ID with negative value? Looks wired."
                         "Try positive!")
    else:
        try:
            db = connect()
            cursor = db.cursor()
            sql = "insert into tournaments (id, name) values (%s, %s);"
            cursor.execute(sql, (id, bleach.clean(name),))
            db.commit()
        except:  # catch *all* exceptions
            print "Oops, unable to register new tournament due to"\
                  "following error:", traceback.format_exc()
            db.rollback()
            raise
        finally:
            db.close()


def registerPlayer(id, name, tournamentId=1):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    if id < 1:
        raise ValueError("Tournament ID with negative value? Looks wired."
                         " Try positive!")
    else:
        try:
            db = connect()
            cursor = db.cursor()
            sql = "insert into players (id, name, fk_tournament) values "\
                  " (%s, %s, %s);"
            cursor.execute(sql, (id, bleach.clean(name), tournamentId,))
            db.commit()
        except:  # catch *all* exceptions
            print "\nOops, unable to register new player due to"\
                  "following error:", traceback.format_exc()
            db.rollback()
            raise
        finally:
            db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    players = []
    db = connect()
    cursor = db.cursor()
    sql = "select * from reportmatches;"  # see reportmatches view.
    cursor.execute(sql)
    players = cursor.fetchall()
    db.close()
    return players


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    if winner != loser:
        try:
            db = connect()
            cursor = db.cursor()
            sql = "insert into matches (fk_player1, fk_player2, fk_winner)"\
                  "values (%s, %s, %s);"
            cursor.execute(sql, (winner, loser, winner,))
            db.commit()
        except:  # catch *all* exceptions
            print "Oops, unable to register the match due to "\
                  "following error:", traceback.format_exc()
            db.rollback()
            raise
        finally:
            db.close()
    else:
        print "Something is wrong! winner and loser can not be the same \
                person."


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairs = []
    try:
        db = connect()
        cursor = db.cursor()
        sql = "select a.id , a.name, b.id, b.name from reportmatches as a,"\
              "reportmatches as b where a.totalwin = b.totalwin and "\
              "a.records = b.records and (a.id < b.id);"
        cursor.execute(sql)
        pairs = cursor.fetchall()
    except:  # catch *all* exceptions
        print "Oops, unable to register the match due to "\
              "following error:", traceback.format_exc()
        raise
    finally:
        db.close()
    return pairs
